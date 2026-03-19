

# getOrElse

Returns this Optional's value if present, or otherwise the result of the defaultValue function.

```kotlin
inline fun <T> Optional<out T & Any>.getOrElse(defaultValue: () -> T): T(source)
```

```kotlin
import java.util.Optional

fun main() {
    val optional: Optional<Int> = Optional.ofNullable(null)   // an empty Optional
    val value = optional.getOrElse { 42 }                     // default value if empty
    println(value)                                           // prints 42
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm.optionals/get-or-else.html)

    