var Toast = function () {
    function showToast(type, message, title, buttonText, buttonLink) {
        const isSnackBar = !!buttonText;

        const toastOptions = {
            closeButton: isSnackBar,
            timeOut: isSnackBar ? 0: 8000,
            tapToDismiss: false,
            positionClass: "toast-bottom-left",            
            extendedTimeOut: isSnackBar ? 0 : 1000
        };

        if (isSnackBar) {
            message = `
                ${message}
                <a href='${buttonLink}' class='btn btn-md'>${buttonText}</a>
            `;
        }

        let iconClass = '';

        switch (type) {
            case 'error':
                iconClass = 'fa-exclamation-circle';
                break;

            case 'success':
                iconClass = 'fa-check-circle';
                break;
        }

        title = `<span class='h5'><i class='far ${iconClass}'></i>${title}</span>`;

        switch (type) {
            case 'error':
                abp.notify.error(message, title, toastOptions);
                break;

            case 'success':
                abp.notify.success(message, title, toastOptions);
                break;
        }
    }

    return {
        errorToast(message, title) {
            showToast('error', message, title);
        },

        successToast(message, title) {
            showToast('success', message, title);
        },

        errorSnackBar(message, title, buttonText, buttonLink) {
            showToast('error', message, title, buttonText, buttonLink);
        },

        successSnackBar(message, title, buttonText, buttonLink) {
            showToast('success', message, title, buttonText, buttonLink);
        },
    }
}();
