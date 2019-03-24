## Skillshare download tool

Simple code that automatically download whole Skillshare course

**Note**: For private use only, please do not share or sell the videos you download.

**Prequisites**:

1. Python >= 3.2
1. [geckodriver](https://github.com/mozilla/geckodriver/releases) (works well with v0.24.0, older versions were not tested and are not recommended). Make sure it is in your `PATH`.
1. Firefox browser
1. Skillshare premium account

**Instruction**:

1. Clone the repository
1. With an editor, open file `account.py` and enter your Skillshare login email and password.
1. Open terminal, type: `python3 download.py {url-of-the-course}`, press Enter/Return.
1. Wait for some minutes for the videos to be downloaded. The program prints `All done` when all the videos are downloaded.

**Some issues**:

1. The account and password you enter are not sent anywhere, except for to log in Skillshare site. Currently there is no other option to log in.
1. If for some reasons, the download did not complete (lose of connection,...), the script will skip all the downloaded files the next time you run it. So if some files were incompletely downloaded, remove them before re-running the script.
1. The videos are saved inside a subfolder, whose name is the course's name, of the repository folder.

