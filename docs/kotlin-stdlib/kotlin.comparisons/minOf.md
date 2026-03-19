

# minOf

Returns the smaller of three values according to the order specified by the given comparator.

```kotlin
fun <T> minOf(a: T, b: T, c: T, comparator: Comparator<in T>): T(source)
```

```kotlin
data class Person(val name: String, val age: Int)

val alice   = Person("Alice",   30)
val bob     = Person("Bob",     25)
val charlie = Person("Charlie", 35)

val youngest = minOf(alice, bob, charlie, compareBy { it.age })

println(youngest)   // Person(name=Bob, age=25)
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.comparisons/min-of.html)

    