

# cast

Casts the given value to the class represented by this KClass object. Throws an exception if the value is null or if it is not an instance of this class.

```kotlin
fun <T : Any> KClass<T>.cast(value: Any?): T(source)
```

```kotlin
import kotlin.reflect.*

fun main() {
    val any: Any = 123
    val number: Int = Int::class.cast(any)
    println(number)  // prints 123
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.reflect/cast.html)

    