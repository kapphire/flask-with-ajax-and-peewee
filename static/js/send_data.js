(($) => {
    $(document)
    .on("click", '#sendData', (event) => {
        let adTitle = $('#adTitle').val();
        let jobTitle = $('#jobTitle').val();
        let adType = $('#adType').val();
        let payType = $('#payType').val();
        let website = $('#website').val();
        let adPrice = $('#adPrice').val();
        let currency = $('#currency').val();
        let country = $('#country').val();
        let state = $('#state').val();
        let city = $('#city').val();
        let adDetail = $('#adDetail').val();
        $.ajax({
            url: "/ajaxData/",
            data: JSON.stringify({
                'adTitle' : adTitle, 
                'jobTitle' : jobTitle, 
                'adType' : adType, 
                'payType' : payType, 
                'website' : website, 
                'adPrice' : adPrice, 
                'currency' : currency, 
                'country' : country, 
                'state' : state, 
                'city' : city, 
                'adDetail' : adDetail
            }),
            contentType: "application/json",
            type: 'POST',
            success: (response) => {
                console.log(response);
            },
            error: (error) => {
                console.log(error);
            }
        });
    })
})(jQuery);

