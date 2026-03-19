

# javaPrimitiveType

Returns a Java Class instance representing the primitive type corresponding to the given KClass if it exists.

```kotlin
val <T : Any> KClass<T>.javaPrimitiveType: Class<T>?(source)
```

```kotlin
import kotlin.jvm.javaPrimitiveType

fun main() {
    val intPrim   = Int::class.javaPrimitiveType      // -> int
    val doublePrim = Double::class.javaPrimitiveType  // -> double
    val stringPrim = String::class.javaPrimitiveType // -> null (not a primitive)

    println("Int   primitive class: $intPrim")
    println("Double primitive class: $doublePrim")
    println("String primitive class: $stringPrim")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/java-primitive-type.html)

    