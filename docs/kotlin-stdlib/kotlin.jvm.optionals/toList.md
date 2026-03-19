

# toList

Returns a new read-only list of this Optional's value if present, or otherwise an empty list. The returned list is serializable (JVM).

```kotlin
fun <T : Any> Optional<out T>.toList(): List<T>(source)
```

```kotlin
import java.util.Optional

fun main() {
    val present: Optional<String> = Optional.of("kotlin")
    val absent: Optional<String>   = Optional.empty()

    println(present.toList())   // prints: [kotlin]
    println(absent.toList())    // prints: []
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm.optionals/to-list.html)

    