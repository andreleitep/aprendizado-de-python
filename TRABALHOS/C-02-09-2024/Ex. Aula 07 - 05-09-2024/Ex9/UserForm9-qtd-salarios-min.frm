VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} UserForm9 
   Caption         =   "UserForm1"
   ClientHeight    =   4995
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   4875
   OleObjectBlob   =   "UserForm9-qtd-salarios-min.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "UserForm9"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Private Sub btnLimpar_Click()

txtSalMin.Text = ""
txtSalFun.Text = ""
txtNomFun.Text = ""

LblRes.Caption = ""


End Sub

Private Sub CommandButton2_Click()

Dim SalMin, SalFun, Resultado As Double
Dim NomFun As String

SalMin = Val(txtSalMin.Value)
SalFun = Val(txtSalFun.Value)
NomFun = txtNomFun.Value

Resultado = Round(SalFun / SalMin, 2)

LblRes.Caption = "O funcionário " & NomFun & " recebe " & Str(Resultado) & " Salários mínimos."

End Sub
