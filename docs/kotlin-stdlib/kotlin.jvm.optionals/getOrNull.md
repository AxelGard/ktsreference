

# getOrNull

Returns this Optional's value if present, or otherwise null.

```kotlin
fun <T : Any> Optional<T>.getOrNull(): T?(source)
```

```kotlin
import java.util.Optional

fun main() {
    val present: Optional<String> = Optional.of("Kotlin")
    val absent: Optional<String>  = Optional.empty()

    val presentValue: String? = present.getOrNull()
    val absentValue: String?  = absent.getOrNull()

    println(presentValue) // Kotlin
    println(absentValue)  // null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm.optionals/get-or-null.html)

    