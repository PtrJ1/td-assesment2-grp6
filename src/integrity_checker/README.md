Integrity Check Tool for Assets


Tool Briefing
● This tool provides an integrity check utility to help artists make sure their work is
ready to publish.


Checks
● The tool needs to be able to run in multiple contexts, on multiple types of assets.
● The following integrity checks should be implemented:
  ○ General:
    ■ Remove unknown/unused nodes
    ■ Check asset names match your naming conventions
    ■ Check node hierarchy is correct for publishing
    ■ Check there are no reference errors
    ■ Check attributes for NaN (very small decimals) in asset attributes and round to 4 decimal points
  ○ For layout:
    ■ Check camera aperture is in a 16:9 aspect ratio
    ■ Check the focal length/f-stop values are consistent with real world cameras
      ● Focal length: "12", "14", "16", "18", "21", "25", "27", "32", "35", "40", "50", "65", "75", "100", "135", or "150"
      ● F-stop: "1.3", "2", "2.8", "4", "5.6", "8", "11", "16", or "22"
  ○ For setPieces:
    ■ Check the set transform and pivot is at the origin
  ○ For sets:
    ■ Check the set transform and pivot is at the origin
    ■ Check the most recent version of each set piece model is referenced
      ● Please remember that your tool should work with both Windows and Unix paths.
      
Approach/Methods:

Run checks on selected assets to ensure they meet established standards.
Provide feedback to users if inconsistencies or errors are detected.

Steps to Complete:

Define the standards/criteria for each asset type.
Develop algorithms/scripts to check each criterion.
Build a GUI to display results and provide feedback.
Implement 'fix-it' options if possible, to correct simple issues.

Entails:

Understanding of common issues in Maya assets.
Strong scripting skills to automate checking procedures.

Finished Look:

A tool where users can select assets, run checks, and get a report detailing any issues.
