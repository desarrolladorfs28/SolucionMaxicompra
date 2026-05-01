# 1. Estructura repetitiva de reinicio (para permitir múltiples consultas)
continuar_programa = "si"
while continuar_programa.lower() == "si":
    
    # Datos de entrada
    nombre = input("Nombre del trabajador: ")
    tipo_contrato = input("Tipo de contrato (planilla/honorarios): ").lower()
    monto_mensual = float(input(f"Sueldo/Pago mensual en S/: "))
    
    asignacion_familiar = 0
    if tipo_contrato == "planilla":
        tiene_asig = input("¿Tiene asignación familiar? (si/no): ").lower()
        if tiene_asig == "si":
            # S/ 102.50 mensual / 4 semanas = 25.625
            asignacion_familiar = 25.625

    # Primera Etapa – Registro de la Semana
    especial = input("¿Tuvo vacaciones, ausentismo, feriados o licencias? (si/no): ").lower()
    
    if especial == "si":
        print("Debe dirigirse a Recursos Humanos para el procesamiento de su pago.")
    else:
        total_horas_extras = 0
        pago_base_semanal = monto_mensual / 4 
        jornada_incompleta = False

        # 2. Estructura repetitiva principal (Iteración de los 5 días)
        for dia in range(1, 6):
            # 3. Estructura repetitiva de validación de entrada
            while True:
                try:
                    horas = float(input(f"Horas trabajadas el día {dia}: "))
                    if horas >= 0:
                        break
                    else:
                        print("Las horas no pueden ser negativas.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")

            if horas < 8:
                print("El día califica como jornada parcial. Comuníquese con RRHH.")
                jornada_incompleta = True
                break # El proceso se detiene por no cumplir jornada
            elif horas > 8:
                total_horas_extras += (horas - 8)

        if not jornada_incompleta:
            # Segunda etapa: Cálculo del pago
            valor_hora_normal = (monto_mensual / 30) / 8
            monto_horas_extras = total_horas_extras * (valor_hora_normal * 2)

            if tipo_contrato == "planilla":
                sueldo_bruto = pago_base_semanal + asignacion_familiar + monto_horas_extras
                # AFP Hábitat 13.21%
                descuento_afp = sueldo_bruto * 0.1321
                
                # Impuesto a la renta (Simplificado: si anual > 7 UIT)
                impuesto_renta = 0
                if (monto_mensual * 14) > 36050:
                    impuesto_renta = sueldo_bruto * 0.08
                
                sueldo_neto = sueldo_bruto - descuento_afp - impuesto_renta

                # Salidas Planilla
                print("\n--- RESUMEN DE PAGO (PLANILLA) ---")
                print(f"Sueldo semanal base: S/ {pago_base_semanal:.2f}")
                print(f"Asignación familiar: S/ {asignacion_familiar:.2f}")
                print(f"Horas extras ({total_horas_extras}h): S/ {monto_horas_extras:.2f}")
                print(f"Sueldo Bruto: S/ {sueldo_bruto:.2f}")
                print(f"Descuento AFP Hábitat: S/ {descuento_afp:.2f}")
                print(f"Impuesto a la Renta: S/ {impuesto_renta:.2f}")
                print(f"SUELDO NETO FINAL: S/ {sueldo_neto:.2f}")

            else: # Recibo por Honorarios
                remun_bruta = pago_base_semanal + monto_horas_extras
                
                retencion_cuarta = 0
                if remun_bruta > 1500:
                    retencion_cuarta = remun_bruta * 0.08
                
                remun_neta = remun_bruta - retencion_cuarta

                # Salidas Honorarios
                print("\n--- RESUMEN DE PAGO (HONORARIOS) ---")
                print(f"Remuneración semanal base: S/ {pago_base_semanal:.2f}")
                print(f"Horas adicionales ({total_horas_extras}h): S/ {monto_horas_extras:.2f}")
                print(f"Remuneración Bruta: S/ {remun_bruta:.2f}")
                print(f"Retención 4ta Categoría: S/ {retencion_cuarta:.2f}")
                print(f"REMUNERACIÓN NETA FINAL: S/ {remun_neta:.2f}")

    print("-" * 40)
    continuar_programa = input("¿Desea realizar otro cálculo? (si/no): ")

print("Gracias por usar la calculadora de Maxicompra.")