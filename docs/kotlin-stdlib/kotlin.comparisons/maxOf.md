

# maxOf

Returns the greater of three values according to the order specified by the given comparator.

```kotlin
fun <T> maxOf(a: T, b: T, c: T, comparator: Comparator<in T>): T(source)
```

```kotlin
data class Person(val name: String, val age: Int)

fun main() {
    val alice = Person("Alice", 30)
    val bob   = Person("Bob",   25)
    val carol = Person("Carol", 35)

    val oldest = maxOf(alice, bob, carol, Comparator.comparingInt { it.age })
    println("Oldest person: ${oldest.name} (${oldest.age})")   // prints: Oldest person: Carol (35)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.comparisons/max-of.html)

    