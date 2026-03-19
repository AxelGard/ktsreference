

# toCollection

Appends this Optional's value to the given destination collection if present.

```kotlin
@IgnorableReturnValuefun <T : Any, C : MutableCollection<in T>> Optional<T>.toCollection(destination: C): C(source)
```

```kotlin
import java.util.Optional

fun main() {
    val optionalValue: Optional<String> = Optional.of("Kotlin")
    val destination = mutableListOf<String>()
    optionalValue.toCollection(destination)
    println(destination) // prints: [Kotlin]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm.optionals/to-collection.html)

    