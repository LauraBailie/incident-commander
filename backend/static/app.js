const API = window.location.origin;

window.onload = loadIncidents;

async function loadIncidents(){

try {

    const response = await fetch(API + "/incidents");

    if (!response.ok) {
        throw new Error("Backend returned " + response.status);
    }

    const incidents = await response.json();

    let html = "";

    incidents.forEach(i => {

        html += `
        <div class="card">
            <h3>${i.title}</h3>
            <p>Status: ${i.status}</p>
            <p>Severity: ${i.severity}</p>
        </div>
        `;

    });

    document.getElementById("incidents").innerHTML = html;

}
catch(err){

    console.error(err);

    document.getElementById("incidents").innerHTML =
        "<p>Unable to load incidents.</p>";

}

}

async function createIncident(){

    await fetch(API + "/incidents",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            title:document.getElementById("title").value,
            description:document.getElementById("description").value,
            severity:document.getElementById("severity").value,
            status:"Open",
            service:document.getElementById("service").value

        })

    });

    document.getElementById("title").value="";
    document.getElementById("description").value="";
    document.getElementById("service").value="";

    loadIncidents();

}

async function investigate() {

    const response = await fetch(API + "/commander/investigate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            question: document.getElementById("question").value
        })
    });

    const result = await response.json();

    document.getElementById("analysis").textContent = `
ROOT CAUSE
----------
${result.root_cause}

IMMEDIATE ACTIONS
-----------------
• ${result.immediate_actions.join("\n• ")}

LONG TERM ACTIONS
-----------------
• ${result.long_term_actions.join("\n• ")}

CONFIDENCE
----------
${result.confidence}%
`;
}

loadIncidents()

async function searchIncidents(){

    const response = await fetch(API + "/search", {

        method: "POST",

        headers:{
            "Content-Type":"application/json"
        },

        body: JSON.stringify({

            question:
            document.getElementById("searchText").value

        })

    });

    const results = await response.json();

    let html = "";

    results.forEach(i=>{

        html += `
        <div>

        <h3>${i.title}</h3>

        <p><b>Severity:</b> ${i.severity}</p>

        <p>${i.summary}</p>

        <hr>

        </div>
        `;

    });

    document.getElementById("searchResults").innerHTML = html;

}