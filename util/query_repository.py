
gastos = "SELECT public.gasto.name, sum(op_gasto.saldo) " \
          " FROM public.operacion_gasto op_gasto" \
          " INNER JOIN public.gasto ON public.gasto.id = op_gasto.gasto" \
          " WHERE op_gasto.fecha BETWEEN '{}' AND '{}'" \
          " GROUP BY op_gasto.gasto, public.gasto.name" \
          " ORDER BY sum(op_gasto.saldo) DESC;"

ingresos = "SELECT public.ingreso.name, sum(op_ingreso.saldo) " \
          " FROM public.operacion_ingreso op_ingreso" \
          " INNER JOIN public.ingreso ON public.ingreso.id = op_ingreso.ingreso" \
          " WHERE op_ingreso.fecha BETWEEN '{}' AND '{}'" \
          " GROUP BY op_ingreso.ingreso, public.ingreso.name" \
          " ORDER BY sum(op_ingreso.saldo) DESC;"