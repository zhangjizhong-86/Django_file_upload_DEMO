# Django_file_upload_DEMO
## A simple Django file upload DEMO

There are 3 templates.
- file_upload_input_submit.html: interacts with a **input**.
- file_upload_hide_input_function_in_href.html: interacts with a hyperlink, whose click function lies in a javascript inside \<head\>.
- file_upload_hide_input_with_function.html: interacts with a hyperlink, whose one-line click function simplified into href itself.

### views.py
upload function deals with the file uploaded, and redirects to a report DEMO page, which contains the filename.
