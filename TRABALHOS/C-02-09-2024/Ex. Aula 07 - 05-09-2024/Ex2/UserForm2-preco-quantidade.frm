VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} UserForm2 
   Caption         =   "UserForm1"
   ClientHeight    =   3285
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   7080
   OleObjectBlob   =   "UserForm2-preco-quantidade.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "UserForm2"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Private Sub BtnRes_Click()

Dim Preco, Resultado As Double
Dim Quantidade As Integer

Preco = Val(TxtPrUn.Value)
Quantidade = Val(TxtQt.Value)
Resultado = Preco * Quantidade
LblRes = "R$" & Str(Resultado)

End Sub
