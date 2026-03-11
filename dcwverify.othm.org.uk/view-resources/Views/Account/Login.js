var AccountLogin = function () {
    let config = {
        returnUrl: "",
    };

    var showErrorMsg = function (form, type, msg) {
        var alert = $('<div class="alert alert-' + type + ' fade show" role="alert">' +
            '                            <div class="alert-icon"><i class="flaticon-questions-circular-button"></i></div>' +
            '                            <div class="alert-text">' + msg + '</div>' +
            '                            <div class="alert-close">' +
            '                                <button type="button" class="close" data-dismiss="alert" aria-label="Close">' +
            '                                    <span aria-hidden="true"><i class="la la-close"></i></span>' +
            '                                </button>' +
            '                            </div>' +
            '                        </div>');

        form.find('.alert').remove();
        alert.prependTo(form);
        mUtil.animateClass(alert[0], 'fadeIn animated');
        alert.find('span').html(msg);
    };

    var handleSignInFormSubmit = function () {

        $('#m_login_signin_submit').click(function (e) {
            e.preventDefault();

            var btn = $(this);
            var form = $(this).closest('form');

            form.validate({
                rules: {
                    usernameOrEmailAddress: {
                        required: true
                    },
                    password: {
                        required: true
                    }
                }
            });

            if (!form.valid()) {
                return;
            }

            btn.addClass('m-loader m-loader--right m-loader--light').disabled = true;

            form.ajaxSubmit(
                {
                    url: '/account/login',
                    complete: function (response, status, xhr, $form)
                    {

                        btn.removeClass('m-loader m-loader--right m-loader--light').disabled = false;

                        if (response.responseJSON.success)
                        {
                            window.location = response.responseJSON.targetUrl;
                        }
                        else
                        {
                            var message = response.responseJSON.error.details === null ? response.responseJSON.error.message : response.responseJSON.error.details;
                            showErrorMsg(form, 'danger', message);
                        }
                    }
                });
        });
    };

    function initRegisterNavBarLink() {
        $("#kt_header a[href='/registration']").attr("href", `/registration?returnUrl=${encodeURIComponent(config.returnUrl)}`);
    }

    return {
        init: function (customConfig) {
            config = $.extend(true, {}, config, customConfig);

            handleSignInFormSubmit();

            if (config.returnUrl)
                initRegisterNavBarLink();
        },
    };
}();
