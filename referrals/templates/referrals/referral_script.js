{% load cache %}
{% cache 600 referral_script %}
	window.onload = function() {

    var getUrlParameter = function getUrlParameter(sParam) {
        var sPageURL = decodeURIComponent(window.location.search.substring(1)),
            sURLVariables = sPageURL.split('&'),
            sParameterName,
            i;

        for (i = 0; i < sURLVariables.length; i++) {
            sParameterName = sURLVariables[i].split('=');

            if (sParameterName[0] === sParam) {
                return sParameterName[1] === undefined ? true : sParameterName[1];
            }
        }
    };

		var referralLink = getUrlParameter('ref');
		var referral = localStorage.getItem('{{ prefix }}referralLink');

		if (typeof referralLink !== "undefined") {
			localStorage.setItem('{{ prefix }}referralLink', referralLink)
		};

		if (typeof referral === "undefined" || referral === null) {
			localStorage.setItem('{{ prefix }}referralLink', '{{ default_value }}' ) 
		};
		
	}
{% endcache %}