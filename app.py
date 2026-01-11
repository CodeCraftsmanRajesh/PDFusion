from flask import Flask, render_template, request, send_file, flash
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from io import BytesIO
import zipfile


app = Flask(__name__)
app.secret_key = "secret"


@app.route("/")
def index():
    return render_template("index.html")

# ---------------- MERGE PDFs ----------------
@app.route("/merge", methods=["GET", "POST"])
def merge_pdf():
    if request.method == "POST":
        files = request.files.getlist("pdfs")

        if len(files) < 2:
            flash("Please upload at least 2 PDF files")
            return render_template("merge.html")

        merger = PdfMerger()

        for file in files:
            merger.append(file.stream)

        output_pdf = BytesIO()
        merger.write(output_pdf)
        merger.close()
        output_pdf.seek(0)

        return send_file(
            output_pdf,
            as_attachment=True,
            download_name="merged_pdfusion.pdf",
            mimetype="application/pdf"
        )

    return render_template("merge.html")


# ---------------- SPLIT PDFs ----------------
@app.route("/split", methods=["GET", "POST"])
def split_pdf():
    if request.method == "POST":

        # ---------- VALIDATION ----------
        if "pdf" not in request.files:
            flash("No PDF file uploaded")
            return render_template("split.html")

        file = request.files["pdf"]
        pages_input = request.form.get("pages", "").strip()

        if file.filename == "":
            flash("Please select a PDF file")
            return render_template("split.html")

        if not pages_input:
            flash("Please select page numbers")
            return render_template("split.html")

        # ---------- READ PDF ----------
        try:
            reader = PdfReader(file.stream)
        except Exception:
            flash("Invalid or corrupted PDF file")
            return render_template("split.html")

        total_pages = len(reader.pages)

        # ---------- PARSE PAGE NUMBERS ----------
        try:
            selected_pages = sorted(
                set(int(p.strip()) for p in pages_input.split(","))
            )
        except ValueError:
            flash("Invalid page format. Use numbers separated by commas.")
            return render_template("split.html")

        # ---------- PAGE RANGE CHECK ----------
        if any(p < 1 or p > total_pages for p in selected_pages):
            flash(f"Page numbers must be between 1 and {total_pages}")
            return render_template("split.html")

        # ---------- SPLIT LOGIC ----------
        selected_writer = PdfWriter()
        remaining_writer = PdfWriter()

        selected_indexes = set(p - 1 for p in selected_pages)

        for i in range(total_pages):
            if i in selected_indexes:
                selected_writer.add_page(reader.pages[i])
            else:
                remaining_writer.add_page(reader.pages[i])

        # ---------- CREATE PDFs IN MEMORY ----------
        selected_pdf = BytesIO()
        remaining_pdf = BytesIO()

        selected_writer.write(selected_pdf)
        remaining_writer.write(remaining_pdf)

        # ---------- ZIP BOTH FILES ----------
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
            zipf.writestr("selectedPages_pdfusion.pdf", selected_pdf.getvalue())
            zipf.writestr("remainingPages_pdfusion.pdf", remaining_pdf.getvalue())

        zip_buffer.seek(0)

        # ---------- SEND ZIP ----------
        return send_file(
            zip_buffer,
            as_attachment=True,
            download_name="split_results.zip",
            mimetype="application/zip"
        )

    # ---------- GET REQUEST ----------
    return render_template("split.html")



if __name__ == "__main__":
    app.run()
