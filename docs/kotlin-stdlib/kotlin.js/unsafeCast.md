

# unsafeCast

Reinterprets this value as a value of the specified type T without any actual type checking.

```kotlin
inline fun <T> Any?.unsafeCast(): T(source)
```

```kotlin
import kotlin.js.*

// A Kotlin data class that matches the shape of the JavaScript object
data class Person(val name: String, val age: Int)

fun main() {
    // Simulate receiving a plain JavaScript object (dynamic) from an API
    val raw: dynamic = js("{ name: 'Alice', age: 30 }")

    // Reinterpret the dynamic object as a Person without any runtime type checks
    val person = raw.unsafeCast<Person>()

    // Now `person` is treated as a typed Kotlin object
    println("${person.name} is ${person.age} years old")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.js/unsafe-cast.html)

    