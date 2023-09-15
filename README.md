# td-assesment2-grp6
Technical Direction for 3D Animation and Graphics Projects (41801) Assessment Task 2: Developing Part of a 3D Animation / VFX Pipeline

Students are required to work in small groups with individual tasks to create tools for a section of
a 3D animation / VFX pipeline. Based on a specific brief, they plan and execute the development
of these tools using industry standard workflows. Deliverables include, functional computer code,
documentation and evidence of Agile methodologies and usage of Git.

Part 1
Each member of the group will present at least one section of the presentation which will contain
the following:

● Production schedule and plan (group assessed) which contains:
   ○ A schedule for the work, with milestones, and the student who is assigned to work
   on each tool.
   ○ Planned folder structure with Work in Progress (WIP) and Publish areas.
   ○ Data types to be passed between departments.
   
● Pseudocode for each tool to be developed (individually assessed)

● A Git repository, which academic staff will need to been given access to

Part 2
Each individual will present the tool they have developed to show that it works in conjunction with the
other tools developed by their group.
Groups will also present the following:

● Functional computer code that works with both Unix and Windows file paths

● User documentation for each tool

● Usage of a Git repository showing the frequency and quality of commits for each individual
student in the group

Repository Structure:

  src/: Source code for all tools.
  
                  asset_publisher/: Code for the asset publishing system.
    
                  integrity_checker/: Code for the asset integrity check tool.
    
                  lighting_scene_builder/: Code for the tool that builds a lighting scene.
    
  docs/: Documentation for each tool.
  
  tests/: Temp folder to test unfinished or rough scripts and assets to verify the functionality of tools.
  
  assets/: Sample 3D assets for demo purposes.
  
  .gitignore: A file specifying patterns of files/folders that Git should ignore. (e.g., *.pyc, *.log, etc.)
