import React from 'react';

function PowerBIDashboard() {
    return (
        <div>
            <h1>Power BI Dashboard</h1>
            <iframe
                title="Power BI"
                width="100%"
                height="600"
                src="https://app.powerbi.com/view?r=YOUR_EMBED_LINK"
                frameBorder="0"
                allowFullScreen={true}
            ></iframe>
        </div>
    );
}

export default PowerBIDashboard;
