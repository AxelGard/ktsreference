

# annotationClass

Returns a KClass instance corresponding to the annotation type of this annotation.

```kotlin
val <T : Annotation> T.annotationClass: KClass<out T>(source)
```

```kotlin
@Target(AnnotationTarget.CLASS)
annotation class Greeting(val message: String)

@Greeting("Hello, world!")
class Greeter

fun main() {
    val ann = Greeter::class.annotations.filterIsInstance<Greeting>().first()
    val kClass = ann.annotationClass
    println(kClass)                                 // prints class Greeting
    println(kClass == Greeting::class)              // true
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/annotation-class.html)

    