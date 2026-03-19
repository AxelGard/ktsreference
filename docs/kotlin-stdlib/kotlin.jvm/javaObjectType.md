

# javaObjectType

Returns a Java Class instance corresponding to the given KClass instance. In case of primitive types it returns corresponding wrapper classes.

```kotlin
val <T : Any> KClass<T>.javaObjectType: Class<T>(source)
```

```kotlin
import kotlin.reflect.KClass

fun main() {
    // Kotlin class reference
    val kotlinString: KClass<String> = String::class
    val javaStringClass = kotlinString.javaObjectType
    println("Kotlin String class -> Java: ${javaStringClass.name}") // prints java.lang.String

    // Primitive type example
    val kotlinInt: KClass<Int> = Int::class
    val javaIntClass = kotlinInt.javaObjectType
    println("Kotlin Int class -> Java: ${javaIntClass.name}") // prints java.lang.Integer
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/java-object-type.html)

    