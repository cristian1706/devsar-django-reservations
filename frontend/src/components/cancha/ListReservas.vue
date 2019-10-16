<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                
                <div>
                    <h2>Reservas</h2>
                    <b-button size="sm" :to="{name: 'NewReserva', params:{reservaId: reservaId, canchaId: canchaId } }" variant="primary">Nueva reserva</b-button>
                </div>
                <br>
                
                <div class="col-md-12">
                    <b-table striped hover :items="reservas" :fields="fields">
                        
                        <template v-slot:cell(action)="row">
                            <b-button size="sm" variant="primary" :to="{ name:'EditReserva', params:{reservaId: row.item.id, canchaId: canchaId } }">
                                Editar
                            </b-button>
                            <b-button size="sm" variant="danger" :to="{ name:'DeleteReserva', params:{reservaId: row.item.id, canchaId: canchaId } }">
                                Borrar
                            </b-button>
                        </template>

                    </b-table>
                </div>

                <div class="rows">
                        <div class="col text-left">
                            
                            <b-button type="submit" class="btn-large-space" :to="{ name: 'ListCanchas' }">Volver</b-button>
                        </div>
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
            canchaId: this.$route.params.canchaId,
            reservaId: this.$route.params.reservaId,
            fields: [
                { key: 'cancha', label: 'Cancha' },
                { key: 'cliente', label: 'Cliente' },
                { key: 'empleado', label: 'Empleado' },
                { key: 'turno_reserva', label: 'Turno reserva' },
                { key: 'action', label: '' }
            ],
            reservas: []
        }
    },
    methods: {
        
        getReservas() {
            const path = `http://localhost:8000/reservas/?canchaId=${this.canchaId}`
            axios.get(path).then((response) => {
                this.reservas = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        }
    },
    created() {
        this.getReservas()
    }
}
</script>

<style lang="css" scoped>
</style>