

# associateByTo

Populates and returns the destination mutable map with key-value pairs, where key is provided by the keySelector function applied to each element of the given sequence and value is the element itself.

```kotlin
@IgnorableReturnValueinline fun <T, K, M : MutableMap<in K, in T>> Sequence<T>.associateByTo(destination: M, keySelector: (T) -> K): M(source)
```

```kotlin
fun main() {
    // A sequence of names
    val names = listOf("Alice", "Bob", "Charlie", "Anna").asSequence()

    // Destination mutable map
    val map: MutableMap<Char, String> = mutableMapOf()

    // Populate the map where the key is the first letter of each name
    val result = names.associateByTo(map) { it.first() }

    // Print the resulting map
    println(result)          // {A=Anna, B=Bob, C=Charlie}
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/associate-by-to.html)

    