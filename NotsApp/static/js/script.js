document.getElementById('priority').addEventListener('change', function() {
        var selectedOption = this.options[this.selectedIndex];
        var priority = selectedOption.value;
        var currentUrl = window.location.href;

        if (currentUrl.includes('priority=')) {
            currentUrl = currentUrl.replace(/priority=\w+/, 'priority=' + priority);
        } else {
            currentUrl += (currentUrl.includes('?') ? '&' : '?') + 'priority=' + priority;
        }
        window.location.href = currentUrl;
});