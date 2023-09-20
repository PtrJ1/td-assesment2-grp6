# pseudocode version with boolean functions that return true or false that makes it more modular, makes the functions reusable, and makes testing more straightfoward

FUNCTION main():

    # GUI Initialization
    CREATE a GUI window with necessary buttons and logs

    IF user clicks "Run Integrity Check" button:
        CALL runIntegrityCheck()

FUNCTION runIntegrityCheck():

    # General Checks
    IF NOT removeUnknownOrUnusedNodes():
        LOG "Unknown or unused nodes found."
    IF NOT isAssetNamingConventionValid():
        LOG "Asset naming convention error."
    IF NOT isNodeHierarchyValid():
        LOG "Node hierarchy error."
    IF NOT areReferencesValid():
        LOG "Reference error."
    CALL checkAttributesForNaN()

    # Context Specific Checks
    IF context is "Layout":
        IF NOT isCameraApertureValid():
            LOG "Aperture error."
        IF NOT isFocalLengthAndFStopValid():
            LOG "Invalid focal length or f-stop."

    ELSE IF context is "SetPieces" OR "Sets":
        IF NOT isTransformAndPivotAtOrigin():
            LOG "Transform/Pivot error."
        IF context is "Sets" AND NOT isLatestVersionOfSetPiece():
            LOG "Outdated setPiece."

FUNCTION removeUnknownOrUnusedNodes():
    FOUND = False
    FOR each node in the scene:
        IF node is unknown OR unused:
            DELETE node
            FOUND = True
    RETURN NOT FOUND

FUNCTION isAssetNamingConventionValid():
    FOR each asset in the scene:
        IF asset name does NOT match naming convention:
            RETURN False
    RETURN True

FUNCTION isNodeHierarchyValid():
    FOR each node in the scene:
        IF node hierarchy is incorrect:
            RETURN False
    RETURN True

FUNCTION areReferencesValid():
    FOR each reference in the scene:
        IF reference has error:
            RETURN False
    RETURN True

FUNCTION checkAttributesForNaN():
    FOR each attribute in the assets:
        IF attribute value is NaN:
            ROUND attribute to 4 decimal points

FUNCTION isCameraApertureValid():
    FOR each camera in the scene:
        IF camera aperture is NOT 16:9:
            RETURN False
    RETURN True

FUNCTION isFocalLengthAndFStopValid():
    FOR each camera in the scene:
        IF focal length NOT in given list:
            RETURN False
        IF f-stop NOT in given list:
            RETURN False
    RETURN True

FUNCTION isTransformAndPivotAtOrigin():
    FOR each set OR setPiece in the scene:
        IF transform OR pivot is NOT at the origin:
            RETURN False
    RETURN True

FUNCTION isLatestVersionOfSetPiece():
    FOR each setPiece referenced in the scene:
        IF version of setPiece is NOT the latest:
            RETURN False
    RETURN True
