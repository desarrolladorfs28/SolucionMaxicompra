def obtener_dias_habiles(mes):

    nombre_meses = [
        "enero", "febrero", "marzo", "abril",
        "mayo", "junio", "julio", "agosto",
        "setiembre", "octubre", "noviembre", "diciembre"
    ]

    dias_laborables = [
        21, 20, 22, 20,
        20, 21, 20, 20,
        22, 21, 21, 20
    ]

    for i in range(len(nombre_meses)):

        if mes == nombre_meses[i]:

            return dias_laborables[i]

    return 20


def registrar_horas():

    total_horas_extras = 0
    jornada_incompleta = False

    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes"]

    for dia in dias_semana
    :

        while True:

            try:

                horas = float(
                    input(f"Horas trabajadas el día {dia}: ")
                )

                if horas >= 0:
                    break

                else:
                    print("Las horas no pueden ser negativas.")

            except ValueError:

                print("Ingrese un número válido.")

        # Jornada parcial
        if horas < 8:

            print()
            print("Jornada parcial.")
            print("Comuníquese con RRHH.")

            jornada_incompleta = True

            break

        # Horas extras
        elif horas > 8:

            total_horas_extras += (horas - 8)

    return total_horas_extras, jornada_incompleta


def calcular_planilla(
    monto_mensual,
    dias_habiles,
    total_horas_extras
):

    pago_base_semanal = monto_mensual * 5 / dias_habiles

    tiene_asig = input(
        "¿Tiene asignación familiar? (si/no): "
    ).lower()

    asignacion_familiar = 0

    if tiene_asig == "si":

        asignacion_familiar = 113 * 5 / dias_habiles

    valor_hora_normal = (monto_mensual / 30) / 8

    monto_horas_extras = (
        total_horas_extras * (valor_hora_normal * 2)
    )

    sueldo_bruto = (
        pago_base_semanal
        + asignacion_familiar
        + monto_horas_extras
    )

    descuento_afp = sueldo_bruto * 0.1137

    impuesto_renta = 0

    if (monto_mensual * 14) > 38500:

        impuesto_renta = sueldo_bruto * 0.08

    sueldo_neto = (
        sueldo_bruto
        - descuento_afp
        - impuesto_renta
    )

    print("\n------ RESUMEN PLANILLA ------")

    print(f"Sueldo semanal: S/ {pago_base_semanal:.2f}")

    print(
        f"Asignación familiar: "
        f"S/ {asignacion_familiar:.2f}"
    )

    print(
        f"Horas extras ({total_horas_extras}h): "
        f"S/ {monto_horas_extras:.2f}"
    )

    print(f"Sueldo bruto: S/ {sueldo_bruto:.2f}")

    print(f"AFP: S/ {descuento_afp:.2f}")

    print(f"Renta: S/ {impuesto_renta:.2f}")

    print(f"SUELDO NETO: S/ {sueldo_neto:.2f}")


def calcular_honorarios(
    monto_mensual,
    dias_habiles,
    total_horas_extras
):

    pago_base_semanal = monto_mensual * 5 / dias_habiles

    valor_hora_normal = (monto_mensual / 30) / 8

    monto_horas_extras = (
        total_horas_extras * (valor_hora_normal * 2)
    )

    remun_bruta = (
        pago_base_semanal
        + monto_horas_extras
    )

    retencion_cuarta = 0

    if monto_mensual > 1500:

        retencion_cuarta = remun_bruta * 0.08

    remun_neta = (
        remun_bruta
        - retencion_cuarta
    )

    print("\n------ RESUMEN HONORARIOS ------")

    print(
        f"Remuneración semanal: "
        f"S/ {pago_base_semanal:.2f}"
    )

    print(
        f"Horas extras ({total_horas_extras}h): "
        f"S/ {monto_horas_extras:.2f}"
    )

    print(f"Remuneración bruta: S/ {remun_bruta:.2f}")

    print(
        f"Retención 4ta: "
        f"S/ {retencion_cuarta:.2f}"
    )

    print(f"REMUNERACIÓN NETA: S/ {remun_neta:.2f}")


def iniciar_calculo():

    print("\n===== REGISTRO DEL TRABAJADOR =====")

    nombre = input("Nombre del trabajador: ")

    monto_mensual = float(
        input("Sueldo mensual S/: ")
    )

    mes = input(
        "Mes de cálculo: "
    ).lower()

    dias_habiles = obtener_dias_habiles(mes)

    especial = input(
        "¿Tuvo vacaciones, ausentismo, "
        "feriados o licencias? (si/no): "
    ).lower()

    if especial == "si":

        print()
        print(
            "Debe dirigirse a Recursos Humanos."
        )

        return

    total_horas_extras, jornada_incompleta = (
        registrar_horas()
    )

    if jornada_incompleta:

        return

    tipo_contrato = input(
        "Tipo de contrato "
        "(planilla/honorarios): "
    ).lower()

    if tipo_contrato == "planilla":

        calcular_planilla(
            monto_mensual,
            dias_habiles,
            total_horas_extras
        )

    else:

        calcular_honorarios(
            monto_mensual,
            dias_habiles,
            total_horas_extras
        )


def main():

    while True:

        print("\n========== MAXICOMPRA ==========")
        print("1. Iniciar cálculo de pago")
        print("2. Salir")
        print("================================")

        opcion = input("Seleccione una opción: ")

        # INICIAR
        if opcion == "1":

            iniciar_calculo()

        # SALIR
        elif opcion == "2":

            print()
            print(
                "Gracias por usar el sistema "
                "de Maxicompra."
            )

            break

        # OPCIÓN INVÁLIDA
        else:

            print()
            print("Opción incorrecta.")


main()
