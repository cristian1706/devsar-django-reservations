<template lang="html">
    <div class="container">
        
        <div class="row">
            <div class="col text-left">
                <h2>Nueva reserva</h2>
            </div>
        </div>
        
        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        
                        <form @submit="onSubmit">
                            
                            <label for="cancha" class="col-form-label">Seleccione una cancha</label>
                            <b-form-select v-model="form.cancha">
                                <template v-slot:first>
                                    <option value="" disabled>-- Por favor seleccione una opción --</option>
                                    <option :value="cancha.id" v-for="cancha in canchas">{{ cancha.nombre_cancha }}</option>
                                </template>
                            </b-form-select>
                            <br><br>

                            <div class="form-group row">
                                <label for="cliente" class="col-sm-2 col-form-label">Cliente</label>
                                <div class="col-sm-6">
                                    <input type="text" placeholder="Ingrese cliente" name="cliente" class="form-control" v-model.trim="form.cliente">
                                </div>
                            </div>

                            <label for="empleado" class="col-form-label">Empleado</label>
                            <b-form-select v-model="form.empleado">
                                <template v-slot:first>
                                    <option value="" disabled>-- Por favor seleccione una opción --</option>
                                    <option :value="usuario.id" v-for="usuario in usuarios">{{ usuario.username }}</option>
                                </template>
                            </b-form-select>
                            <br><br>

                            <div class="form-group row">
                                <label for="turno" class="col-sm-2 col-form-label">Turno reserva</label>
                                <div class="col-sm-6">
                                    <input type="datetime" placeholder="2019-10-15T14:57:48.672170-03:00" name="turno" class="form-control" v-model="form.turno_reserva">
                                </div>
                            </div>

                            <div class="rows">
                                <div class="col text-left">
                                    <b-button type="submit" variant="primary">Crear</b-button>
                                    <b-button type="submit" class="btn-large-space" :to="{ name: 'ListReservas', params:{reservaId: reservaId, canchaId: canchaId } }">Cancelar</b-button>
                                </div>
                            </div>
                        
                        </form>
                    
                    </div>
                </div>
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
            reservaId: this.$route.params.reservaId,
            canchaId: this.$route.params.canchaId,
            form: {
                cancha: 0,
                cliente: '',
                empleado: 0,
                turno_reserva: ''
            },
            canchas: [],
            usuarios: []
        }
    },
    methods: {
        onSubmit(evt) {
            evt.preventDefault()

            const path = 'http://localhost:8000/reservas/'

            axios.post(path, this.form).then((response) => {
                this.form.cancha = response.data.cancha
                this.form.cliente = response.data.cliente
                this.form.empleado = response.data.empleado
                this.form.turno_reserva = response.data.turno_reserva
                swal("Reserva creada exitosamente!", "", "success")
                this.$router.push('/canchas')
            })
            .catch((error) => {
                console.log(error)
                swal("La reserva no pudo crearse", "", "error")
            })
        },

         getCanchas() {
            const path = 'http://localhost:8000/canchas/'
            axios.get(path).then((response) => {
                this.canchas = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        },

        getUsers() {
            const path = 'http://localhost:8000/usuarios/'
            axios.get(path).then((response) => {
                this.usuarios = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        },
    },

    created() {
        this.getCanchas()
        this.getUsers()
    }
}
</script>

<style lang="css" scoped>
</style>