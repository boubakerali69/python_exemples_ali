var a100=10
var b100=20

open class personne1{
    var nom:String?=null
    var prenom:String?=null
    var age:Int?=null

     constructor(nom:String,prenom:String,age:Int){
        this.nom=nom
        this.prenom=prenom
        this.age=age

    }


    
    fun afficher(){
        println("nom = $nom  prénom= $prenom  aga = $age")
    }
    open fun calculer(){

        println("somme = ${a100+b100}")
    }

}

class professeur:personne1("Balsem","boubaker",16){
    fun afficher2(){
        println("bonjour Mr $nom $prenom votre age est $age")
    }
    override fun calculer(){
       super.calculer()
        println("Produit = ${a100*b100}")
    }

        }



fun main(args: Array<String>) {

    var p1=personne1("ali","Boubaker",50)
    p1.afficher()
    var p2=professeur()
    p2.afficher2()
    p2.calculer()


}
