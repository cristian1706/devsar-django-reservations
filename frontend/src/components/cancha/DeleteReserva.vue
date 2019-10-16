<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col">
          
                <h2>Está seguro que desea borrar esta reserva?</h2>
                <p>Cancha: {{ this.element.cancha }}</p>
                <p>Turno reserva: {{ this.element.turno_reserva }}</p>

            </div>
        </div>

        <div class="row">
            <div class="col">
                <b-button v-on:click="deleteReserva" variant="danger">Borrar</b-button>
                <b-button type="submit" class="btn-large-space" :to="{ name: 'ListReservas', params:{reservaId: reservaId, canchaId: canchaId } }">Cancelar</b-button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert'

export default {
    data() {
        return {
            canchaId: this.$route.params.canchaId,
            reservaId: this.$route.params.reservaId,
            element: {
                cancha: '', 
                turno_reserva: ''
            }
        }
    },
    methods: {
        getReserva() {
            const path = `http://localhost:8000/reservas/${this.reservaId}/`

            axios.get(path).then((response) => {
                this.element.cancha = response.data.cancha
                this.element.turno_reserva = response.data.turno_reserva
            })
            .catch((error) => {
                console.log(error)
            })
        },
        deleteReserva() {
            const path = `http://localhost:8000/reservas/${this.reservaId}/`

            axios.delete(path).then((response) => {
                swal("Reserva borrada exitosamente!", "", "success")
                this.$router.push('/canchas')
            })
            .catch((error) => {
                console.log(error)
                swal("No ha sido posible eliminar la reserva", "", "error")
            })
        }
    },
    created() {
        this.getReserva()
    }
}
</script>

<style lang="css" scoped>
</style>