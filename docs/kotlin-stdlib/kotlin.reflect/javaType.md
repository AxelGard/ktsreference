

# javaType

Returns a Java Type instance corresponding to the given Kotlin type.

```kotlin
@ExperimentalStdlibApival KType.javaType: Type(source)
```

```kotlin
import kotlin.reflect.*
import kotlin.reflect.full.starProjectedType
import java.lang.reflect.Type

@OptIn(ExperimentalStdlibApi::class)
fun main() {
    // Kotlin type for String
    val kotlinType: KType = String::class.starProjectedType

    // Corresponding Java Type
    val javaType: Type = kotlinType.javaType

    println(javaType.typeName)   // prints "java.lang.String"
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.reflect/java-type.html)

    