{{/*
Expand the name of the chart.
*/}}
{{- define "postgresql.fullname" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}
