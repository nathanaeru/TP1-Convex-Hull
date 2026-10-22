# Algoritma Divide & Conquer untuk Convexhull
TP1 Geometri Komputasional

## Members
Nathanael Leander Herdanatra - 2406421320
Hasanul Muttaqin - 2406413331

## How to Run
1. Ensure you have Python 3 installed on your system.
2. Create a new venv (recommended)
   **For Windows**
    ```powershell
    python -m venv env
    ```
    **For Unix-like systems (macOS, Linux)**
    ```bash
    python3 -m venv env
    ```
3. Start the venv
   **For Windows**
    ```powershell
    env\Scripts\activate
    ```
    **For Unix-like systems (macOS, Linux)**
    ```bash
    source env/bin/activate
    ```
4. Install all dependencies
    ```bash
    pip install -r requirements.txt
    ```
5. Run the main file
   ```bash
   python main.py
   ```

## How to Test
This repo includes a unit test file located on [_test.py](-test.py). To run it:
1. Ensure you have already installed `pytest`. It should already be on the requirement file, if not:
   ```bash
   pip install pytest
   ```
3. Run the test
   ```bash
   pytest
   ```

## References
Andjani, J. (2015). Penerapan Algoritma Divide and Conquer pada Algoritma Convex Hull. Retrieved October 22, 2026, from https://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2014-2015/Makalah2015/Makalah_IF221_Strategi_Algoritma_2015_078.pdf

GeeksforGeeks. (2017, May 28). Convex hull using divide and conquer algorithm. GeeksforGeeks. https://www.geeksforgeeks.org/dsa/convex-hull-using-divide-and-conquer-algorithm/

Toth, P. R. (2026). Convex Hull algorithm (Divide and conquer) implementation in Go. [Computer software] GitHub. https://github.com/peter-roland-toth/convex-hull-go

GitHub Copilot (built-in from VSCode, used for code suggestions and fixes)
