main function
  create gui 
  if user runs integrity check:
    run integrity check

FUNCTION runIntegrityCheck():
    # General Checks
    call removeUnknownOrUnusedNodes()
    call checkAssetNamingConventions()
    call checkNodeHierarchy()
    call checkReferenceErrors()
    call checkAttributesForNaN()

    # Context Specific Checks
    IF context is "Layout":
        CALL checkCameraAperture()
        CALL checkFocalLengthAndFStop()
    ELSE IF context is "SetPieces" OR "Sets":
        CALL checkTransformAndPivotAtOrigin()

        IF context is "Sets":
            CALL checkLatestVersionOfSetPiece()  
  


FUNCTION removeUnknownOrUnusedNodes():
    // Code to remove unknown/unused nodes

FUNCTION checkAssetNamingConvention() -> BOOLEAN:
    // Code to verify if asset names match naming conventions
    // RETURN True if they match, otherwise False

FUNCTION checkNodeHierarchy() -> BOOLEAN:
    // Code to verify if node hierarchy is correct for publishing
    // RETURN True if correct, otherwise False

FUNCTION hasReferenceErrors() -> BOOLEAN:
    // Code to check for reference errors
    // RETURN True if there are errors, otherwise False

FUNCTION checkAndRoundAttributes():
    // Code to check attributes for NaN and round them to 4 decimal points

FUNCTION checkCameraAperture():
    // Code to check if camera aperture is in 16:9 aspect ratio

FUNCTION checkCameraFocalLength():
    // Code to verify the focal length against the provided values

FUNCTION checkCameraFStop():
    // Code to verify the f-stop value against the provided values

FUNCTION checkTransformAndPivotAtOrigin():
    // Code to ensure the set's transform and pivot is at the origin

FUNCTION checkMostRecentVersionOfSetPieces():
    // Code to verify if the most recent version of each set piece model is referenced
