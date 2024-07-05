# Common Details for an Endpoint #
"""
    @apiDescription Create Endpoint
    Following errors code has been considered in our system.

    @api {post} /api/v1/dummy/dont-hit/ Dummy Endpoint

    @apiName Dummy Endpoint
    @apiGroup 0.Common

    @apiHeader {String} SPEEDY-API-TOKEN JWT access token
    @apiHeader {String} Content-Type application/json

    @apiParam {String} param1 If Param1 is a required parameter
    @apiParam {String} [param2] If Param2 is an optional parameter

    @apiError   BadRequest Bad Request Data / Malformed request. 400
    @apiError   AuthenticationFailed Failed to Authenticate the user. 401
    @apiError   NotFound Not found 404
    @apiError   MethodNotAllowed method not allowed to access 405
    @apiError   PermissionError 403

    @apiError  (Customise Error Codes for NotAuthorizedRequest) InvalidToken Token is invalid/expired code: 452
    @apiError  (Customise Error Codes for NotAuthorizedRequest) SessionNotExists User session doesn't exist code: 453
    @apiError  (Customise Error Codes for NotAuthorizedRequest) TokenNotProvided Token is not provided code: 454

"""
