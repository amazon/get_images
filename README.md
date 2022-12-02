# Test exersise for the interview.

Please write a Python script/application. The script's requirements:

Inputs:
- Mandatory:
  * URL
  * Output directory path
- Optional:
  * Username
  * Password

Outputs:
- Files in the output directory the script downloads based on the extraction rule
explained below

- The script should use Basic Auth when optional username and password specified
- The script should support redirections
- Extraction rule: only the files specified as a source for <img> HTML tag and having .png
(case-insensitive) extension should be downloaded
- Dynamic <img> tags generated by JavaScript can be ignored, i.e., only the original source
code can be evaluated
- The script should be “production-ready”, whatever it means for you
