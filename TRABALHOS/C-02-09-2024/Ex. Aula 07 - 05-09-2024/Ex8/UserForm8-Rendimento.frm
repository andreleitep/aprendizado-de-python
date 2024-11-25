VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} UserFormRendimento 
   Caption         =   "UserForm2"
   ClientHeight    =   5260
   ClientLeft      =   110
   ClientTop       =   450
   ClientWidth     =   6920
   OleObjectBlob   =   "UserFormRendimento.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "UserFormRendimento"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub bttLimpar_Click()
txtDeposito.Value = " "
txtJuros.Value = " "
lblRM.Caption = " "
lblTotal.Caption = " "
End Sub

Private Sub bttRender_Click()
Dim D, J, R, T As Integer
D = Val(txtDeposito.Value)
J = Val(txtJuros.Value)
R = (J / 100) * D
T = R + D
lblRM.Caption = Str(R)
lblTotal.Caption = Str(T)
End Sub
