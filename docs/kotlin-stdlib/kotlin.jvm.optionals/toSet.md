

# toSet

Returns a new read-only set of this Optional's value if present, or otherwise an empty set. The returned set is serializable (JVM).

```kotlin
fun <T : Any> Optional<out T>.toSet(): Set<T>(source)
```

```kotlin
import java.util.Optional

fun main() {
    val present: Optional<String> = Optional.of("Hello")
    val empty: Optional<String> = Optional.empty()

    val presentSet: Set<String> = present.toSet()
    val emptySet: Set<String> = empty.toSet()

    println(presentSet) // [Hello]
    println(emptySet)   // []
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm.optionals/to-set.html)

    