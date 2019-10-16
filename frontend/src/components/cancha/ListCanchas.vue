<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                
                <div>
                    <h2>Lista de canchas</h2>
                </div>
                <br>
                
                <div class="col-md-12">
                    <b-table striped hover :items="canchas" :fields="fields">
                        
                        <template v-slot:cell(action)="row">
                            <b-button size="sm" variant="primary" :to="{ name:'ListReservas', params:{canchaId: row.item.id} }">
                                Ver reservas
                            </b-button>
                        </template>

                    </b-table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            fields: [
                { key: 'nombre_cancha', label: 'Cancha' },
                { key: 'tipo_cancha', label: 'Tipo' },
                { key: 'vestuario_disponible', label: 'Vestuario disponible' },
                { key: 'iluminacion', label: 'Iluminación' },
                { key: 'cesped_sintetico', label: 'Cesped sintético' },
                { key: 'action', label: '' }
            ],
            canchas: []
        }
    },
    methods: {
        
        getCanchas() {
            const path = 'http://localhost:8000/canchas/'
            axios.get(path).then((response) => {
                this.canchas = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        }
    },
    created() {
        this.getCanchas()
    }
}
</script>

<style lang="css" scoped>
</style>