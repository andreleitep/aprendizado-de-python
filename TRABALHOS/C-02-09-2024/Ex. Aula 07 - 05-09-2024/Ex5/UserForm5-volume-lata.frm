VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} UserForm5 
   Caption         =   "UserForm1"
   ClientHeight    =   3150
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   4995
   OleObjectBlob   =   "UserForm5-volume-lata.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "UserForm5"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Private Sub CommandButton1_Click()

Dim Altura, Diametro, Raio, Volume As Double

Altura = Val(txtAlt.Value)
Diametro = Val(txtDi)
Raio = Diametro / 2

Volume = 3.14159 * (Raio * Raio) * Altura

LblRes.Caption = Str(Volume) & "cm³"

End Sub

Private Sub CommandButton2_Click()

txtAlt.Text = ""
txtDi.Text = ""
LblRes.Caption = "Resultado"

End Sub
