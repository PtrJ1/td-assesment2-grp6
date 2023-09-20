FUNCTION main()
  #GUI
  create GUI window with buttons and logs
  if user clicks on "Run Integrity Check" button:
    call runIntegrityCheck()

FUNCTION runIntegrityCheck():
    # General Checks
    call removeUnknownOrUnusedNodes()
    call checkAssetNamingConventions()
    call checkNodeHierarchy()
    call checkReferenceErrors()
    call checkAttributesForNaN()

    # Context Specific Checks
    if context is "Layout":
        call checkCameraAperture()
        call checkFocalLengthAndFStop()
    else if context is "SetPieces" or "Sets":
        call checkTransformAndPivotAtOrigin()
    else if context is "Sets":
        call checkLatestVersionOfSetPiece()  


FUNCTION removeUnknownOrUnusedNodes():
    # Code to remove unused nodes
    for each node in the scene:
      if node is unknown or unused:
        delete node

FUNCTION checkAssetNamingConvention():
    # Code to verify if asset names match naming conventions
    for each asset in the scene:
      if asset name does not match naming convention:
        log "Naming convention error at: " + asset name

FUNCTION checkNodeHierarchy():
    # Code to verify if node hierarchy is correct for publishing
    for each node in the scene:
      if node hierachy is incorrect:
        log "Incorrect hierarchy for: " + node name

FUNCTION hasReferenceErrors():
    # Code to check for reference errors
    for each reference in the scene:
      if reference has error:
        log "Reference error at: " + reference name

FUNCTION checkAttributesforNaN():
    # Code to check attributes for NaN and round them to 4 decimal points
    for each attribute in the assests:
      if attribute value is NaN:
        round attribute to 4 decimal points
      
FUNCTION checkCameraAperture():
    # Code to check if camera aperture is in 16:9 aspect ratio
    for each camera in the scene:
      if camera apeture is not in 16:9:
        log "Aperture error at: " + camera name
        
FUNCTION checkFocalLengthAndFStop():
    # Code to check if camera focal length and f-stop are at valid values
    focallengthlist = "12", "14", "16", "18", "21", "25", "27", "32", "35", "40", "50", "65", "75", "100", "135", "150"
    fstoplist = "1.3", "2", "2.8", "4", "5.6", "8", "11", "16", "22"
    for each camera in the scene:
      if focal length is not in focallengthlist:
        log "Invalid focal length at " + camera name
      if f-stop is not in fstoplist:
        log "Invalid f-stop at: " camera name
        
FUNCTION checkTransformAndPivotAtOrigin():
    # Code to ensure the set's transform and pivot is at the origin
    for each set or setpiece in the scene:
      if transform or pivot is not at the origin:
        log "Transform/Pivot error at: " + set/setpiece name

FUNCTION checkMostRecentVersionOfSetPieces():
    # Code to verify if the most recent version of each set piece model is referenced
    for each setpiece referenced in the scene:
      if version of setpiece is not the latest:
        log "Outdated setpiece: " + setpiece name
