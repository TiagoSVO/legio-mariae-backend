console.log('Load Script');
let generateMinute = {
    init: function() {
        const _this = this
        console.log('Módulo Inicializado');
        const generateButtons = document.getElementsByClassName('gm_button');
        for (const generateButton of generateButtons) {
            generateButton.addEventListener('click', async function() {
                await _this.get_data(3)
                console.log('Its working');
            })
        };
    },

    get_data: async function(meeting_id) {
        const targetTextareaMinuteGenerated = document.getElementById('id_description')

        await fetch("/meetings/data_minute/3", {
            method: "GET",
        })
        .then(response => {
            if(!response.ok) {
                throw new Error(`Request faild with status ${response.status}`)
            }
            return response.json()
        })
        .then(data => {
            console.log(data)
            targetTextareaMinuteGenerated.value = data['meeting_text']
        })
        .catch(error => console.log(error))
    }
}

generateMinute.init();