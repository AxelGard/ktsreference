

# typeOf

Returns a runtime representation of the given reified type T as an instance of KType.

```kotlin
inline fun <T> typeOf(): KType(source)
```

```kotlin
import kotlin.reflect.typeOf

fun main() {
    val stringType = typeOf<String>()
    println("KType of String: $stringType")

    val listIntType = typeOf<List<Int>>()
    println("KType of List<Int>: $listIntType")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.reflect/type-of.html)

    