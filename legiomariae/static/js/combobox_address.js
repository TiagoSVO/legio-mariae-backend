$(document).ready(function($){
    $('script').ready(function() {

        let addressComboBox = {
            _options: {
                baseUrlGetStates: '/addresses/states_country_json/',
                baseUrlGetCities: '/addresses/cities_state_json/',
                baseName: $('input[value*=_combobox]')[0].value.split('_combobox')[0],
            },

            _setDefaultOptions: function() {
                this.baseUrlGetStates = this._options.baseUrlGetStates
                this.baseUrlGetCities = this._options.baseUrlGetCities
                this.baseName = this._options.baseName
                this.fieldsetAddressAdminTag = $('#'+this.baseName+'-group')
                this.addRowTag = this.fieldsetAddressAdminTag.find('.add-row')
            },

            init: function(options) {
                this._setDefaultOptions()
                $.extend(this._options, options || {})

                //Inicializa o evento quando os campos do form já existirem
                this.initEventAddressForm(event)

                //Adiciona um EventListener de onclick para poder trabalhar os dados de endereço
                this.addRowTag.on('click', this.attachEventAddressForm.bind(this))
            },

            attachEventAddressForm: function(event) {
                this.initEventAddressForm(event)
            },

            initEventAddressForm: function(event) {
                let $dynamicFormSet = this.fieldsetAddressAdminTag.find('.dynamic-'+this.baseName).last()
                if ($dynamicFormSet[0]){
                    let $countrySelectTag = $dynamicFormSet.find('select[id*=id_'+$dynamicFormSet[0].id+'-country]')
                    let $stateSelectTag = $dynamicFormSet.find('select[id*=id_'+$dynamicFormSet[0].id+'-state]')
                    let $citySelectTag = $dynamicFormSet.find('select[id*=id_'+$dynamicFormSet[0].id+'-city]')

                    this.changeCountrySelectTag($countrySelectTag, $stateSelectTag, $citySelectTag)

                    this.changeStateSelectTag($stateSelectTag, $citySelectTag)

                }
            },

            changeCountrySelectTag: function(countrySelectTag, stateSelectTag, citySelectTag) {
                let $countrySelectTag = $(countrySelectTag)
                $countrySelectTag.on('change', function() {
                    let countryId = $countrySelectTag.find(':selected').val() || "0"
                    let stateId = "0"

                    this.getStatesByCountry(countryId, stateSelectTag)
                    this.getCitiesByState(stateId, citySelectTag)
                }.bind(this))
            },

            changeStateSelectTag: function(stateSelectTag, citySelectTag) {
                let $stateSelectTag = $(stateSelectTag)
                $stateSelectTag.on('change', function() {
                    let stateId = $stateSelectTag.find(':selected').val() || "0"

                    this.getCitiesByState(stateId, citySelectTag)
                }.bind(this))
            },

            requestDataToFill: function(parent_id, selectTag, baseUrl) {
                const _this = this
                let $selectTag = $(selectTag)
                $.ajax({
                    url: baseUrl + parent_id,
                    success: function(data) {
                        _this.fillOptionsSelect($selectTag, data)
                    }
                })
            },

            getStatesByCountry: function(country_id, stateSelect) {
                this.requestDataToFill(country_id, stateSelect, this.baseUrlGetStates)
            },

            getCitiesByState: function(state_id, citySelect) {
                this.requestDataToFill(state_id, citySelect, this.baseUrlGetCities)
            },

            _createSelectsOption: function (optionInput, optionInfo) {
                let newOptionInput = optionInput.cloneNode(true)
                $(newOptionInput).attr('value', optionInfo['value'])
                $(newOptionInput).removeAttr('selected')
                newOptionInput.innerHTML = optionInfo['name']
                return newOptionInput
            },

            _clearSelectTag: function(selectTag) {
                let $selectTag = $(selectTag)
                $selectTag.children().not(':first').remove()
            },

            _setSelectsOptions: function (selectTag, optionsData) {
                let $selectTag = $(selectTag)
                let optionInput = $selectTag.find('option')[0]

                for(indexOption in optionsData) {
                    let optionInfo = optionsData[indexOption]
                    let newOptionInput = this._createSelectsOption(optionInput, optionInfo)
                    $selectTag.append(newOptionInput)
                }
            },

            _setSelectedOption: function(selectTag, optionIndex=0) {
                let $selectTag = $(selectTag)
                $selectTag.find('option')[0].selected
            },

            fillOptionsSelect: function(selectTag, optionsData) {
                this._clearSelectTag(selectTag)
                this._setSelectsOptions(selectTag, optionsData)
                this._setSelectedOption(selectTag)
            },

        }

        addressComboBox.init()

    })
});