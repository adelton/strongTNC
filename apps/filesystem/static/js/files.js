function setupDirectoryDropdown(url) {
    $('input#dir').select2({
        minimumInputLength: 3,
        formatSelection: function (o) {
            return o.directory
        },
        formatResult: function (o) {
            return o.directory
        },
        query: function (query) {
            autocompleteDelay.ajaxUrl = url;
            autocompleteDelay.callback = query.callback;
            autocompleteDelay.errorCallback = function() {
                alert('Error: Could not fetch directory list.');
            };
            autocompleteDelay.queryUpdate(query.term);
        }
    });
}

function initValidation() {
    $('#fileform').validate($.extend(validationDefaults, {
        rules: {
            'name': {
                required: true,
                maxlength: 255
            },
            'dir': {
                required: true
            }
        },
        ignore: ''
    }));
}
