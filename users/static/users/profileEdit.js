$(document).ready(function () {
    $("#id_techskills").select2({
        multiple: true,
        allowClear: true,
        tags: true,
        tokenSeparators: [','],
        createTag: function (params) {
            var term = $.trim(params.term);
            if (term === '') {
                return null;
            }
            return {
                id: term,
                text: term.toUpperCase(),
                newTag: true // add additional parameters
            }
        },
        insertTag: function (data, tag) {
            // Insert the tag at the end of the results
            data.push(tag);
        },
        templateResult: function (data) {
            var $result = $("<span></span>");
            $result.text(data.text);
            if (data.newTag) {
                $result.append(" <em>(create new tag)</em>");
            }
            return $result;
        },

    }).on('select2:select', function (e) {
        var newTagTitle = e.params.data.text;
        $.ajax({
            type: "GET",
            url: `/tag/new/?newTagTitle=${newTagTitle}`,
            success: function (response) {
                data = $('#id_techskills').val();

                if (response.status == "ok") {
                    var newOption = new Option(response.tag_title, response.tag_id, false, false);
                    $('#id_techskills').append(newOption);
                    data.pop();
                    data.push(newOption.value);
                }
                else if (response.status == "tag already exists") {
                    data.push(response.tag_id);
                }

                $('#id_techskills').val(null).trigger('change');
                $('#id_techskills').val(data).trigger('change');

            }
        })
    });
});