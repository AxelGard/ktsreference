

# associateByTo

Populates and returns the destination mutable map with key-value pairs, where key is provided by the keySelector function applied to each element of the given array and value is the element itself.

```kotlin
@IgnorableReturnValueinline fun <T, K, M : MutableMap<in K, in T>> Array<out T>.associateByTo(destination: M, keySelector: (T) -> K): M(source)
```

```kotlin
data class Person(val id: Int, val name: String)

val people = arrayOf(
    Person(1, "Alice"),
    Person(2, "Bob"),
    Person(3, "Charlie")
)

val personById = mutableMapOf<Int, Person>()
people.associateByTo(personById) { it.id }

println(personById)  // {1=Person(id=1, name=Alice), 2=Person(id=2, name=Bob), 3=Person(id=3, name=Charlie)}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/associate-by-to.html)

    