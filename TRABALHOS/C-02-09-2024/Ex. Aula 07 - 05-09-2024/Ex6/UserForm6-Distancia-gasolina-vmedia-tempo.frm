VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} UserForm6 
   Caption         =   "UserForm3"
   ClientHeight    =   3465
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   6780
   OleObjectBlob   =   "UserForm6-Distancia-gasolina-vmedia-tempo.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "UserForm6"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Private Sub CommandButton1_Click()

Dim Distancia, Litros, VMedia, Tempo As Double

Tempo = Val(txtTempo.Value)
VMedia = Val(txtVelocidade)

Distancia = Tempo * VMedia
Litros = Round(Distancia / 12, 3)

LblRes.Caption = "Velocidade Média: " & Str(VMedia) & "km/h" & Chr(13) & "Tempo Gasto: " & Str(Tempo) & "h" & Chr(13) & "Distância Percorrida: " & Str(Distancia) & "km" & Chr(13) & "Gasolina Gasta: " & Str(Litros) & "L"

End Sub
