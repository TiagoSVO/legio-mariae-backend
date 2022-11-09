console.log('Load Script');
let generateMinute = {
    init: function() {
        const _this = this
        const generateButtons = document.getElementsByClassName('gm_button');

        for (const generateButton of generateButtons) {
            generateButton.addEventListener('click', async function() {
                const MeetingSelectTag = document.querySelector('#id_meeting')
                await _this.get_data(MeetingSelectTag.value)
            })
        };
    },

    get_data: async function(meeting_id) {
        if(!meeting_id) return
        const targetTextareaMinuteGenerated = document.getElementById('id_description')

        await fetch("/meetings/data_minute/"+meeting_id, {
            method: "GET",
        })
        .then(response => {
            if(!response.ok) {
                throw new Error(`Request faild with status ${response.status}`)
            }
            return response.json()
        })
        .then(data => {
            targetTextareaMinuteGenerated.value = data['meeting_text']
        })
        .catch(error => console.log(error))
    }
}

generateMinute.init();